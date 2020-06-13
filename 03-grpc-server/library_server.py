from concurrent import futures
import logging

import grpc

import libraryapi_pb2
import libraryapi_pb2_grpc


class Library(libraryapi_pb2_grpc.LibraryServicer):

    def GetBooks(self, request, context):
        books = [
            libraryapi_pb2.Book(id = 1, name = 'The Hitchhiker\'s Guide to the Galaxy'),
            libraryapi_pb2.Book(id = 2, name = 'The Restaurant at the End of the Universe'),
            libraryapi_pb2.Book(id = 3, name = 'Life, the Universe and Everything'),
            libraryapi_pb2.Book(id = 4, name = 'So Long, and Thanks for All the Fish'),
            libraryapi_pb2.Book(id = 5, name = 'Mostly Harmless'),
            ]
        return libraryapi_pb2.GetBooksReply(books=books)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    libraryapi_pb2_grpc.add_LibraryServicer_to_server(Library(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
