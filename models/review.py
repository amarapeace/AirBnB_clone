#!/usr/bin/python3
'''review.py
'''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' Class for City'''

    place_id = ""
    user_id = ""
    text = ""
