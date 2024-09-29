import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('ready', () => {
  console.log("Redis client connected to the server");
});

subscriber.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  } else {
    console.log(`${message}`);
  }
})
