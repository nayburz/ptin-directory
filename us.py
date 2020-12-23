# TODO: move this module to some package

from datetime import datetime

# Current apportionment to the states, or "T" for territories sending a delegate
# or resident commissioner. This dict is used to filter out the historical territories
# from lists of the current states and territories.
stateapportionment = {'AL': 7, 'AK': 1, 'AS': 'T', 'AZ': 9, 'AR': 4, 'CA': 53, 'CO': 7, 'CT': 5, 'DE': 1, 'DC': 'T', 'FL': 27, 'GA': 14, 'GU': 'T', 'HI': 2, 'ID': 2, 'IL': 18, 'IN': 9, 'IA': 4, 'KS': 4, 'KY': 6, 'LA': 6, 'ME': 2, 'MD': 8, 'MA': 9, 'MI': 14, 'MN': 8, 'MS': 4, 'MO': 8, 'MT': 1, 'NE': 3, 'NV': 4, 'NH': 2, 'NJ': 12, 'NM': 3, 'NY': 27, 'NC': 13, 'ND': 1, 'MP': 'T', 'OH': 16, 'OK': 5, 'OR': 5, 'PA': 18, 'PR': 'T', 'RI': 2, 'SC': 7, 'SD': 1, 'TN': 9, 'TX': 36, 'UT': 4, 'VT': 1, 'VI': 'T', 'VA': 11, 'WA': 10, 'WV': 3, 'WI': 8, 'WY': 1}
#stateapportionment_112 = {'AL': 7, 'AK': 1, 'AS': 'T', 'AZ': 8, 'AR': 4, 'CA': 53, 'CO': 7, 'CT': 5, 'DE': 1, 'DC': 'T', 'FL': 25, 'GA': 13, 'GU': 'T', 'HI': 2, 'ID': 2, 'IL': 19, 'IN': 9, 'IA': 5, 'KS': 4, 'KY': 6, 'LA': 7, 'ME': 2, 'MD': 8, 'MA': 10, 'MI': 15, 'MN': 8, 'MS': 4, 'MO': 9, 'MT': 1, 'NE': 3, 'NV': 3, 'NH': 2, 'NJ': 13, 'NM': 3, 'NY': 29, 'NC': 13, 'ND':  1, 'MP': 'T', 'OH': 18, 'OK': 5, 'OR': 5, 'PA': 19, 'PR': 'T', 'RI': 2, 'SC': 6, 'SD': 1, 'TN': 9, 'TX': 32, 'UT': 3, 'VT': 1, 'VI': 'T', 'VA': 11, 'WA': 9, 'WV': 3, 'WI': 8, 'WY': 1}

# All state abbreviations, including historical territories.
stateabbrs = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA", "WV", "WI", "WY", "DK", "PI", "OL"]

# All state names, including historical territories.
statenames = {"AL":"Alabama", "AK":"Alaska", "AS":"American Samoa", "AZ":"Arizona", "AR":"Arkansas", "CA":"California", "CO":"Colorado", "CT":"Connecticut", "DE":"Delaware", "DC":"District of Columbia", "FL":"Florida", "GA":"Georgia", "GU":"Guam", "HI":"Hawaii", "ID":"Idaho", "IL":"Illinois", "IN":"Indiana", "IA":"Iowa", "KS":"Kansas", "KY":"Kentucky", "LA":"Louisiana", "ME":"Maine", "MD":"Maryland", "MA":"Massachusetts", "MI":"Michigan", "MN":"Minnesota", "MS":"Mississippi", "MO":"Missouri", "MT":"Montana", "NE":"Nebraska", "NV":"Nevada", "NH":"New Hampshire", "NJ":"New Jersey", "NM":"New Mexico", "NY":"New York", "NC":"North Carolina", "ND": "North Dakota", "MP":"Northern Mariana Islands", "OH":"Ohio", "OK":"Oklahoma", "OR":"Oregon", "PA":"Pennsylvania", "PR":"Puerto Rico", "RI":"Rhode Island", "SC":"South Carolina", "SD":"South Dakota", "TN":"Tennessee", "TX":"Texas", "UT":"Utah", "VT":"Vermont", "VI":"Virgin Islands", "VA":"Virginia", "WA":"Washington", "WV":"West Virginia", "WI":"Wisconsin", "WY":"Wyoming", "DK": "Dakota Territory", "PI": "Philippines", "OL": "Territory of Orleans"}
state_abbr_from_name = dict((v.lower(),k) for (k,v) in statenames.items())

# Current states, a list of (abbr, name) tuples in sorted order.
statelist = [s for s in statenames.items() if s[0] in stateapportionment]
statelist.sort(key=lambda x : x[1])

statenames_apstyle = { "AL": "Ala.", "AK": "Alaska", "AZ": "Ariz.", "AR": "Ark.", "CA": "Calif.", "CO": "Colo.", "CT": "Conn.", "DE": "Del.", "FL": "Fla.", "GA": "Ga.", "HI": "Hawaii", "ID": "Idaho", "IL": "Ill.", "IN": "Ind.", "IA": "Iowa", "KS": "Kan.", "KY": "Ky.", "LA": "La.", "ME": "Maine", "MD": "Md.", "MA": "Mass.", "MI": "Mich.", "MN": "Minn.", "MS": "Miss.", "MO": "Mo.", "MT": "Mont.", "NE": "Neb.", "NV": "Nev.", "NH": "N.H.", "NJ": "N.J.", "NM": "N.M.", "NY": "N.Y.", "NC": "N.C.", "ND": "N.D.", "OH": "Ohio", "OK": "Okla.", "OR": "Ore.", "PA": "Pa.", "RI": "R.I.", "SC": "S.C.", "SD": "S.D.", "TN": "Tenn.", "TX": "Texas", "UT": "Utah", "VT": "Vt.", "VA": "Va.", "WA": "Wash.", "WV": "W. Va.", "WI": "Wis.", "WY": "Wyo.", "DC": "District of Columbia" }



# """
# Misspellings/abbreviations mapping.
# A mapping of state misspellings/abbreviations to normalized
# abbreviations, and alphabetical lists of US states, territories,
# military mail regions and non-US states to which the US provides
# postal service.
# This exists in this standalone file so that it's only imported into memory
# when explicitly needed.
# """

# import operator

# from django.utils.functional import lazy
# from django.utils.translation import gettext_lazy as _
# from django.utils.translation import pgettext_lazy

# #: The 48 contiguous states, plus the District of Columbia.
# states = (
#     ('AL', _('Alabama')),
#     ('AZ', _('Arizona')),
#     ('AR', _('Arkansas')),
#     ('CA', _('California')),
#     ('CO', _('Colorado')),
#     ('CT', _('Connecticut')),
#     ('DE', _('Delaware')),
#     ('DC', _('District of Columbia')),
#     ('FL', _('Florida')),
#     ('GA', pgettext_lazy('US state', 'Georgia')),
#     ('ID', _('Idaho')),
#     ('IL', _('Illinois')),
#     ('IN', _('Indiana')),
#     ('IA', _('Iowa')),
#     ('KS', _('Kansas')),
#     ('KY', _('Kentucky')),
#     ('LA', _('Louisiana')),
#     ('ME', _('Maine')),
#     ('MD', _('Maryland')),
#     ('MA', _('Massachusetts')),
#     ('MI', _('Michigan')),
#     ('MN', _('Minnesota')),
#     ('MS', _('Mississippi')),
#     ('MO', _('Missouri')),
#     ('MT', _('Montana')),
#     ('NE', _('Nebraska')),
#     ('NV', _('Nevada')),
#     ('NH', _('New Hampshire')),
#     ('NJ', _('New Jersey')),
#     ('NM', _('New Mexico')),
#     ('NY', _('New York')),
#     ('NC', _('North Carolina')),
#     ('ND', _('North Dakota')),
#     ('OH', _('Ohio')),
#     ('OK', _('Oklahoma')),
#     ('OR', _('Oregon')),
#     ('PA', _('Pennsylvania')),
#     ('RI', _('Rhode Island')),
#     ('SC', _('South Carolina')),
#     ('SD', _('South Dakota')),
#     ('TN', _('Tennessee')),
#     ('TX', _('Texas')),
#     ('UT', _('Utah')),
#     ('VT', _('Vermont')),
#     ('VA', _('Virginia')),
#     ('WA', _('Washington')),
#     ('WV', _('West Virginia')),
#     ('WI', _('Wisconsin')),
#     ('WY', _('Wyoming')),
# )

# #: Non contiguous states (Not connected to mainland USA)
# NON_CONTIGUOUS_STATES = (
#     ('AK', _('Alaska')),
#     ('HI', _('Hawaii')),
# )

# #: Non-state territories.
# US_TERRITORIES = (
#     ('AS', _('American Samoa')),
#     ('GU', _('Guam')),
#     ('MP', _('Northern Mariana Islands')),
#     ('PR', _('Puerto Rico')),
#     ('VI', _('Virgin Islands')),
# )

# #: Military postal "states". Note that 'AE' actually encompasses
# #: Europe, Canada, Africa and the Middle East.
# ARMED_FORCES_STATES = (
#     ('AA', _('Armed Forces Americas')),
#     ('AE', _('Armed Forces Europe')),
#     ('AP', _('Armed Forces Pacific')),
# )

# #: Non-US locations serviced by USPS (under Compact of Free
# #: Association).
# COFA_STATES = (
#     ('FM', _('Federated States of Micronesia')),
#     ('MH', _('Marshall Islands')),
#     ('PW', _('Palau')),
# )

# #: Obsolete abbreviations (no longer US territories/USPS service, or
# #: code changed).
# OBSOLETE_STATES = (
#     ('CM', _('Commonwealth of the Northern Mariana Islands')),  # Is now 'MP'
#     ('CZ', _('Panama Canal Zone')),  # Reverted to Panama 1979
#     ('PI', _('Philippine Islands')),  # Philippine independence 1946
#     # Became the independent COFA states + Northern Mariana Islands 1979-1994
#     ('TT', _('Trust Territory of the Pacific Islands')),
# )

# US_STATES = lazy(lambda: tuple(sorted(
#     states + NON_CONTIGUOUS_STATES,
#     key=operator.itemgetter(0))), tuple)()


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