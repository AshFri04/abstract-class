"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """Initialize abstract melon order. """

    def __init__(self, species, qty):
        """Initiate abstract order."""
        self.species = species
        self.qty = qty
        shipped = False
        base_price = 5

    def get_total(self):
        """Calculate price, including tax."""

        total = (1 + self.tax) * self.qty * self.base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty)
   
    order_type = "international"
    tax = 0.17



