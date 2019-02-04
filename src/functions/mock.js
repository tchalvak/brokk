// Simply mock out a response for get and post endpoints

const get = data => {
  return { mock: true }
}

const mock = (event, context, callback) => {
  const res = get(event)
  const headersSet = {
    'Access-Control-Allow-Origin': '*', // Temporarily allow * CORS for rapid prototyping
    'Access-Control-Allow-Credentials': true,
  }
  callback(null, {
    statusCode: 200,
    body: JSON.stringify(res),
    headers: headersSet,
  })
  return true
}

module.exports = {
  get: mock,
  post: mock,
  put: mock,
  delete: mock,
}

// Example local invocation: sls invoke local --function register --data '{ "mock": "The lambda will return the same regardless of input." }'
