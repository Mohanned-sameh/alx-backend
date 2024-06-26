const blackListed = ['4153518780', '4153518781'];
import { kue } from 'redis';

function sendNotification(phoneNumber, message, job, done) {
  if (blackListed.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});

export default queue;
