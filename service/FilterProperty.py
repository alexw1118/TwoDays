from model import BaseProperty
from service import ViewProperty


def filter_rent(filter_list):
    property_list_for_rent = ViewProperty.rent()
    return custom_filter(filter_list, property_list_for_rent)


def filter_sale(filter_list):
    property_list_for_rent = ViewProperty.sale()
    return custom_filter(filter_list, property_list_for_rent)


def custom_filter(filter_list, property_list_for_rent):
    filtered_property_list = []
    filtered_list = [prop for prop in property_list_for_rent if any(attribute in prop for attribute in filter_list)]
    for filtered_property in filtered_list:
        filtered_property_list.append(vars(BaseProperty.BaseProperty(filtered_property)))
    return filtered_property_list
