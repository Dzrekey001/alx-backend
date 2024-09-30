import kue from 'kue';
import chai from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  }
];
describe('createPushNotificationsJobs', function () {
  let print = {};
  before(function () {
    queue.testMode.enter();
  });
  this.beforeEach(function (){
    print = sinon.spy(console, 'log');
  });
  afterEach(function() {
    queue.testMode.clear();
    print.restore();
  });
  after(function () {
    queue.testMode.exit();
  });
  // test for array requirement
  it('throws an error if jobs is not an array', function() {
    chai.expect(function () { createPushNotificationsJobs('jobs', queue); }).to.throw(Error, 'Jobs is not an array');
  });
  it('create three new jobs on the queue', function() {
    createPushNotificationsJobs(list, queue);
    chai.expect(queue.testMode.jobs.length).to.equal(3);
  });
  it('test that on succesful creation consoles the correct message', function() {
    createPushNotificationsJobs(list, queue);
    chai.expect(print.calledThrice).to.be.true;
    chai.expect(print.calledWith('Notification job created: 4'));
    chai.expect(print.calledWith('Notification job created: 5'));
    chai.expect(print.calledWith('Notification job created: 6'));
  });
});
