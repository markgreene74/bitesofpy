# https://codechalleng.es/bites/216/
import re

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501


def get_email_details(header: str) -> dict:
    """User re.search or re.match to capture the from, to, subject
    and date fields. Return the groupdict() of matching object, see:
    https://docs.python.org/3.7/library/re.html#re.Match.groupdict
    If not match, return None
    """
    # this is one way to solve the exercise
    # result_keys = ["from", "to", "subject", "date"]
    # search_strings = [
    #     r"From\:\s(.*)",
    #     r"To\:\s(.*)",
    #     r"Subject\:\s(.*)",
    #     r"Date\:\s(.*)\s[+-]",
    # ]
    # result_values = [re.search(s, EMAIL_HEADER).group(1) for s in search_strings]
    # print(dict(zip(result_keys, result_values)))

    # or we could use groupdict as suggested
    m = re.search(
        r"From\:\s(?P<from>.*)\n.*To\:\s(?P<to>.*)\n.*Subject\:\s(?P<subject>.+?)\n.*Date\:\s(?P<date>.*)\s[+-]",
        header,
        re.MULTILINE | re.DOTALL,
    )
    return m.groupdict() if m else None
