
const mongoose = require('mongoose');

const postSchema = mongoose.Schema({
  message: { type: String, required: true }
  // creator: { type: mongoose.Schema.Types.ObjectId, ref: "txt", required: true }
});

module.exports = mongoose.model("Message", postSchema);
