
const handler = module.exports = {};

/**
 * 
 * @param {object} options
 * @param {object} options.message
 * @param {integer} options.message.payload.Id
 * @param {string} options.message.payload.TransactionType
 */
handler.PublishBookTransactionCommand = async ({message}) => {
  // Implement your business logic here...
};
