from pydantic import BaseModel

class TransactionSchema(BaseModel):
    transaction_id          : int
    transaction_date        : str
    transaction_operator    : int
    user_name               : str

class TransactionDetailSchema(BaseModel):
    transaction_detail_id           : int
    transaction_detail_transaction  : int
    transaction_detail_product      : int
    transaction_detail_quantity     : int
    transaction_detail_price        : float
    transaction_detail_subtotal     : float
    transaction_product_name        : str

class TransactionDetailRequestSchema(BaseModel):
    product_id                  : int
    quantity_transaction        : int
    product_price               : float
    
class TransactionAndDetailSchema(BaseModel):
    transaction_info                : TransactionSchema
    transaction_details             : list[TransactionDetailSchema]

class TransactionNewRecordSchema(BaseModel):
    transaction_details             : list[TransactionDetailRequestSchema]