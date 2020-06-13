const Router = require('hermesjs/lib/router');
const router = new Router();
const publishBookTransactionHandler = require('../handlers/publish-book-transaction');
module.exports = router;

router.use('publish/book/transaction', async (message, next) => {
  try {
    await publishBookTransactionHandler.PublishBookTransactionCommand({message});
    next();
  } catch (e) {
    next(e);
  }
});
