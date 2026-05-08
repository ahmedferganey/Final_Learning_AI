from .BaseDataModel import BaseDataModel
from .db_schemes import Asset
from .enums.DataBaseEnum import DataBaseEnum
from bson import ObjectId

class AssetModel(BaseDataModel):

    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_ASSET_NAME.value]


    @classmethod
    async def create_instance(cls, db_client: object):
        instance = cls(db_client=db_client)
        await instance.init_collection()
        return instance

    async def init_collection(self):
        self.collection = self.db_client[DataBaseEnum.COLLECTION_ASSET_NAME.value]
        indexes = Asset.get_indexes()

        for index in indexes:
            await self.collection.create_index(
                index["key"],
                name=index["name"],
                unique=index["unique"]
            )

    async def create_asset(self, asset: Asset):

        result = await self.collection.insert_one(
            asset.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)
        )
        asset.id = result.inserted_id

        return asset
    
    async def get_all_project_assets(self, asset_project_id: str, asset_type: str = None):

        query = {
            "asset_project_id": ObjectId(asset_project_id) if isinstance(asset_project_id, str) else asset_project_id
        }

        if asset_type is not None:
            query["asset_type"] = asset_type

        cursor = self.collection.find(query, {"_id": 1, "asset_name": 1})

        assets = {}
        async for record in cursor:
            assets[record["_id"]] = record["asset_name"]

        return assets

    async def get_project_asset_by_name(self, asset_project_id: str, asset_name: str, asset_type: str = None):

        query = {
            "asset_project_id": ObjectId(asset_project_id) if isinstance(asset_project_id, str) else asset_project_id,
            "asset_name": asset_name,
        }

        if asset_type is not None:
            query["asset_type"] = asset_type

        record = await self.collection.find_one(query, {"_id": 1, "asset_name": 1})

        if record is None:
            return {}

        return {
            record["_id"]: record["asset_name"]
        }
