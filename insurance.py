from service import Service


class Insurance(Service):
    """Insurance service offered by bank

    Child class of Service, and potentially future parent class of other types of insurance

    Attributes:
        asset: string of what the asset being insured is.
        asset_value: float or int of the estimated asset value.
        monthly_premium: the amount charged monthly for the insurance
    """

    def __init__(self, asset, asset_value, monthly_premium, account_number, customer_id):
        super().__init__(account_number, customer_id)
        self.asset = asset
        self.asset_value = asset_value
        self.monthly_premium = monthly_premium

    def reimburse_customer(self):
        """after db is set up a query will be run to add the asset value ot the customer's balance."""
