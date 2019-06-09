"""System policies."""
from .const import CAT_ENTITIES, SUBCAT_ALL, POLICY_READ

ADMIN_POLICY = {
    CAT_ENTITIES: True,
}

USER_POLICY = {
    CAT_ENTITIES: True,
}

READ_ONLY_POLICY = {
    CAT_ENTITIES: {
        SUBCAT_ALL: {
            POLICY_READ: True
        }
    }
}
