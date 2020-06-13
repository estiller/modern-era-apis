const Router = require('hermesjs/lib/router');
const router = new Router();
const subscribeBookInventoryHandler = require('../handlers/subscribe-book-inventory');
module.exports = router;

router.useOutbound('subscribe/book/inventory', async (message, next) => {
  try {
    await subscribeBookInventoryHandler.SubscribeBookInventoryUpdates({message});
    next();
  } catch (e) {
    next(e);
  }
});
