from project.exceptions import BadRequestRequeredFieldNotFound, \
    BadRequestFieldNotAllowed


def verify_json(json_data, required_fields, optional_fields=None):
    for field in required_fields:
        if field not in json_data.keys():
            raise BadRequestRequeredFieldNotFound(field)

    if optional_fields is not None:
        all_fields = optional_fields + required_fields
    else:
        all_fields = required_fields

    for field in json_data.keys():
        if field not in all_fields:
            raise BadRequestFieldNotAllowed(field)


def verify_json_field(json_data, required_field):
    if required_field not in json_data.keys():
        raise BadRequestRequeredFieldNotFound(required_field)
