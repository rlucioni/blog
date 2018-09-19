const AWS = require('aws-sdk');

// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html
const s3 = new AWS.S3({
  apiVersion: '2006-03-01',
});

async function sync() {
  // TODO: sync!
}

sync()
  .then(() => {
    console.info('sync complete');
    process.exit(0);
  })
  .catch((err) => {
    console.info('sync failed');
    console.error(err);
    process.exit(1);
  });
