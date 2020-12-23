"""
Misspellings/abbreviations mapping.
A mapping of state misspellings/abbreviations to normalized
abbreviations, and alphabetical lists of US states, territories,
military mail regions and non-US states to which the US provides
postal service.
This exists in this standalone file so that it's only imported into memory
when explicitly needed.
"""

import operator

from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy

#: The 48 contiguous states, plus the District of Columbia.
CONTIGUOUS_STATES = (
    ('AL', _('Alabama')),
    ('AZ', _('Arizona')),
    ('AR', _('Arkansas')),
    ('CA', _('California')),
    ('CO', _('Colorado')),
    ('CT', _('Connecticut')),
    ('DE', _('Delaware')),
    ('DC', _('District of Columbia')),
    ('FL', _('Florida')),
    ('GA', pgettext_lazy('US state', 'Georgia')),
    ('ID', _('Idaho')),
    ('IL', _('Illinois')),
    ('IN', _('Indiana')),
    ('IA', _('Iowa')),
    ('KS', _('Kansas')),
    ('KY', _('Kentucky')),
    ('LA', _('Louisiana')),
    ('ME', _('Maine')),
    ('MD', _('Maryland')),
    ('MA', _('Massachusetts')),
    ('MI', _('Michigan')),
    ('MN', _('Minnesota')),
    ('MS', _('Mississippi')),
    ('MO', _('Missouri')),
    ('MT', _('Montana')),
    ('NE', _('Nebraska')),
    ('NV', _('Nevada')),
    ('NH', _('New Hampshire')),
    ('NJ', _('New Jersey')),
    ('NM', _('New Mexico')),
    ('NY', _('New York')),
    ('NC', _('North Carolina')),
    ('ND', _('North Dakota')),
    ('OH', _('Ohio')),
    ('OK', _('Oklahoma')),
    ('OR', _('Oregon')),
    ('PA', _('Pennsylvania')),
    ('RI', _('Rhode Island')),
    ('SC', _('South Carolina')),
    ('SD', _('South Dakota')),
    ('TN', _('Tennessee')),
    ('TX', _('Texas')),
    ('UT', _('Utah')),
    ('VT', _('Vermont')),
    ('VA', _('Virginia')),
    ('WA', _('Washington')),
    ('WV', _('West Virginia')),
    ('WI', _('Wisconsin')),
    ('WY', _('Wyoming')),
)

#: Non contiguous states (Not connected to mainland USA)
NON_CONTIGUOUS_STATES = (
    ('AK', _('Alaska')),
    ('HI', _('Hawaii')),
)

#: Non-state territories.
US_TERRITORIES = (
    ('AS', _('American Samoa')),
    ('GU', _('Guam')),
    ('MP', _('Northern Mariana Islands')),
    ('PR', _('Puerto Rico')),
    ('VI', _('Virgin Islands')),
)

#: Military postal "states". Note that 'AE' actually encompasses
#: Europe, Canada, Africa and the Middle East.
ARMED_FORCES_STATES = (
    ('AA', _('Armed Forces Americas')),
    ('AE', _('Armed Forces Europe')),
    ('AP', _('Armed Forces Pacific')),
)

#: Non-US locations serviced by USPS (under Compact of Free
#: Association).
COFA_STATES = (
    ('FM', _('Federated States of Micronesia')),
    ('MH', _('Marshall Islands')),
    ('PW', _('Palau')),
)

#: Obsolete abbreviations (no longer US territories/USPS service, or
#: code changed).
OBSOLETE_STATES = (
    ('CM', _('Commonwealth of the Northern Mariana Islands')),  # Is now 'MP'
    ('CZ', _('Panama Canal Zone')),  # Reverted to Panama 1979
    ('PI', _('Philippine Islands')),  # Philippine independence 1946
    # Became the independent COFA states + Northern Mariana Islands 1979-1994
    ('TT', _('Trust Territory of the Pacific Islands')),
)

US_STATES = lazy(lambda: tuple(sorted(
    CONTIGUOUS_STATES + NON_CONTIGUOUS_STATES,
    key=operator.itemgetter(0))), tuple)()


#     public string GetState(State state)
#     {
#         switch (state)
#         {
#             case State.AL:
#                 return "ALABAMA";

#             case State.AK:
#                 return "ALASKA";

#             case State.AS:
#                 return "AMERICAN SAMOA";

#             case State.AZ:
#                 return "ARIZONA";

#             case State.AR:
#                 return "ARKANSAS";

#             case State.CA:
#                 return "CALIFORNIA";

#             case State.CO:
#                 return "COLORADO";

#             case State.CT:
#                 return "CONNECTICUT";

#             case State.DE:
#                 return "DELAWARE";

#             case State.DC:
#                 return "DISTRICT OF COLUMBIA";

#             case State.FM:
#                 return "FEDERATED STATES OF MICRONESIA";

#             case State.FL:
#                 return "FLORIDA";

#             case State.GA:
#                 return "GEORGIA";

#             case State.GU:
#                 return "GUAM";

#             case State.HI:
#                 return "HAWAII";

#             case State.ID:
#                 return "IDAHO";

#             case State.IL:
#                 return "ILLINOIS";

#             case State.IN:
#                 return "INDIANA";

#             case State.IA:
#                 return "IOWA";

#             case State.KS:
#                 return "KANSAS";

#             case State.KY:
#                 return "KENTUCKY";

#             case State.LA:
#                 return "LOUISIANA";

#             case State.ME:
#                 return "MAINE";

#             case State.MH:
#                 return "MARSHALL ISLANDS";

#             case State.MD:
#                 return "MARYLAND";

#             case State.MA:
#                 return "MASSACHUSETTS";

#             case State.MI:
#                 return "MICHIGAN";

#             case State.MN:
#                 return "MINNESOTA";

#             case State.MS:
#                 return "MISSISSIPPI";

#             case State.MO:
#                 return "MISSOURI";

#             case State.MT:
#                 return "MONTANA";

#             case State.NE:
#                 return "NEBRASKA";

#             case State.NV:
#                 return "NEVADA";

#             case State.NH:
#                 return "NEW HAMPSHIRE";

#             case State.NJ:
#                 return "NEW JERSEY";

#             case State.NM:
#                 return "NEW MEXICO";

#             case State.NY:
#                 return "NEW YORK";

#             case State.NC:
#                 return "NORTH CAROLINA";

#             case State.ND:
#                 return "NORTH DAKOTA";

#             case State.MP:
#                 return "NORTHERN MARIANA ISLANDS";

#             case State.OH: 
#                 return "OHIO";

#             case State.OK:
#                 return "OKLAHOMA";

#             case State.OR:
#                 return "OREGON";

#             case State.PW:
#                 return "PALAU";

#             case State.PA:
#                 return "PENNSYLVANIA";

#             case State.PR:
#                 return "PUERTO RICO";

#             case State.RI:
#                 return "RHODE ISLAND";

#             case State.SC:
#                 return "SOUTH CAROLINA";

#             case State.SD:
#                 return "SOUTH DAKOTA";

#             case State.TN:
#                 return "TENNESSEE";

#             case State.TX:
#                 return "TEXAS";

#             case State.UT:
#                 return "UTAH";

#             case State.VT:
#                 return "VERMONT";

#             case State.VI:
#                 return "VIRGIN ISLANDS";

#             case State.VA:
#                 return "VIRGINIA";

#             case State.WA:
#                 return "WASHINGTON";

#             case State.WV:
#                 return "WEST VIRGINIA";

#             case State.WI:
#                 return "WISCONSIN";

#             case State.WY:
#                 return "WYOMING";
#         }

#         throw new Exception("Not Available");
#     }
# }