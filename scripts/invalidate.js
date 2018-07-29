const AWS = require('aws-sdk');

// https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CloudFront.html
const cloudfront = new AWS.CloudFront({
  apiVersion: '2017-10-30',
});

async function invalidate() {
  const distributionId = process.env.CLOUDFRONT_DISTRIBUTION_ID;

  let res = await cloudfront.listDistributions().promise();

  const distribution = res.DistributionList.Items.find(e => e.Id === distributionId);
  const cname = distribution.Aliases.Items[0];

  console.info(`creating invalidation for distribution with CNAME ${cname}`);

  const params = {
    DistributionId: distributionId,
    InvalidationBatch: {
      CallerReference: Date.now().toString(),
      Paths: {
        Quantity: 1,
        Items: [
          '/*',
        ],
      },
    },
  };

  res = await cloudfront.createInvalidation(params).promise();

  const invalidationId = res.Invalidation.Id;
  const invalidationStatus = res.Invalidation.Status;

  console.info(`created invalidation ${invalidationId} with status ${invalidationStatus}`);
}

invalidate()
  .then(() => {
    console.info('invalidation complete');
    process.exit(0);
  })
  .catch((err) => {
    console.info('invalidation failed');
    console.error(err);
    process.exit(1);
  });
