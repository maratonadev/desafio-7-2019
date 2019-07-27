const request = require('request');
require('dotenv').config();

exports.credentials = (req, response) => {

  let body = {
    apikey: process.env.IAM_APIKEY,
    workspace_id: process.env.WORKSPACE_ID,
    desafio: process.env.DESAFIO,
    id: process.env.MARATONA_ID,
    cpf: req.body.cpf
  }
  console.log(body);
  if (req.body.cpf != '') {
    request({
      uri: "https://8d829621.us-south.apiconnect.appdomain.cloud/desafios/desafio7",
      body: body,
      json: true,
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
    }, function (err, res) {
      if (err) {
        response.status(500).json({
          msg: err
        })
        console.log(err);
      } else {
        response.status(200).json({
          msg: res.body
        })
      }
    });
  } else {
    response.status(404).json({
      msg: 'Missing Fields'
    })
  }
}



