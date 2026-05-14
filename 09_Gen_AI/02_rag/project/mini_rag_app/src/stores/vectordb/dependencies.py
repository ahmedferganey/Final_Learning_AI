from fastapi import Request

from stores.vectordb.VectorStoreInterface import VectorStoreInterface


def get_vector_store(request: Request) -> VectorStoreInterface:
    # Created once on app startup.
    return request.app.vector_store

