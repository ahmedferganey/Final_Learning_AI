from .providers import QdrantDBProvider
from .VectorDBEnums import VectorDBEnums
from controllers.BaseController import BaseController

class VectorDBProviderFactory:
    def __init__(self, config):
        self.config = config
        self.base_controller = BaseController()

    def _get_config_value(self, key: str):
        if isinstance(self.config, dict):
            return self.config.get(key)
        return getattr(self.config, key, None)

    def create(self, provider: str):
        if provider == VectorDBEnums.QDRANT.value:
            db_path = self.base_controller.get_database_path(
                self._get_config_value("VECTOR_DB_PATH")
            )
            return QdrantDBProvider(
                db_path=db_path,
                distance_method=self._get_config_value("VECTOR_DB_DISTANCE_METHOD")
            )
        
        return None



