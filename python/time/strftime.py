import datetime

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

_utc = datetime.datetime.utcfromtimestamp
at = _utc(1311272226);

string = at.strftime(TIME_FORMAT)
tz = at.tzinfo.tzname(None) if at.tzinfo else 'UTC'
string += ('Z' if tz == 'UTC' else tz)
print string
