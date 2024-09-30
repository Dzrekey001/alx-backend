import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
];

function getItemById(id) {
  const itemList = listProducts.filter(element => element.id.toString() === id);
  return itemList[0];
}

const app = express();
const port = 1245;
app.get('/list_products', (req, res) => {
  const listJson = [];
  listProducts.forEach(item => {
    let alternativeItem = {};
    alternativeItem['itemId'] = item.id;
    alternativeItem['itemName'] = item.name;
    alternativeItem['price'] = item.price;
    alternativeItem['initialAvailableQuantity'] = item.stock;
    listJson.push(alternativeItem);
  });
  res.json(listJson);
});
app.get('/list_products/:itemId', async (req, res, next) => {
  const itemId = req.params.itemId;
  const alternativeItem = {};
  let reservedStock = null;
  const item = getItemById(itemId);
  if (item == null) {
    alternativeItem['status'] = 'Product not found';
    res.json(alternativeItem);
  } else {
      try {
        reservedStock = await getCurrentReservedStockById(itemId);
      } catch (error) {
          return next(error);
      }
      alternativeItem['itemId'] = item.id;
      alternativeItem['itemName'] = item.name;
      alternativeItem['price'] = item.price;
      alternativeItem['initialAvailableQuantity'] = item.stock;
      if (reservedStock !== null) {
        alternativeItem['currentQuantity'] = item.stock - reservedStock;
      } else {
        alternativeItem['currentQuantity'] = item.stock;
      }
      res.json(alternativeItem);
  }
});
app.get('/reserve_product/:itemId', (req, res, next) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  const alternativeItem = {};
  if (item == null) {
    alternativeItem['status'] = 'Product not found';
    res.json(alternativeItem);
  } else {
    let intItem = 0;
    try {
      intItem = Number(itemId);
    } catch (error) {
      next(error);
    }
    if (item.stock <= 0) {
      alternativeItem['status'] = 'Not enough stock available';
      alternativeItem['itemId'] = intItem;
      res.json(alternativeItem);
    } else {
      reserveStockById(itemId, item.stock);
      alternativeItem['status'] = 'Reservation confirmed';
      alternativeItem['itemId'] = intItem;
      res.json(alternativeItem);
    }
  }
});
app.listen(port);

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  const item = getItemById(itemId);  
  client.set(itemId, stock);
}
async function getCurrentReservedStockById(itemId) {
  
  try {
    const stock = await getAsync(itemId);
    return stock;
  } catch (error) {
    console.error(error);
  }  
}
