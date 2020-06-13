const PROTO_PATH = __dirname + '/../03-grpc-server/proto/libraryapi.proto';

const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const os = require('os');

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });
const library_proto = grpc.loadPackageDefinition(packageDefinition).libraryapi;

function main() {
    const client = new library_proto.Library('localhost:50051', grpc.credentials.createInsecure());
    client.getBooks({}, function (err, response) {
        if (err) {
            console.error(err);
        }
        else {
            console.log(`The books available are:${os.EOL}${JSON.stringify(response.books, null, 1)}`);
        }
    });
}

main();