"""
End-to-end tests that run against the Google server
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import shlex

import utils


def getKey():
    doc = utils.getAuthValues()
    key = doc['google']['key']
    return key


def runTests():
    separator = "----------------------"
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..', 'client_dev.py')
    baseUrl = "https://www.googleapis.com/genomics/v1beta2"
    key = getKey()
    keyStr = "--key {0}".format(key)
    workarounds = "--workarounds=google"
    minimalOutput = "-O"
    commands = [
        "variants-search --variant_set_ids 10473108253681171589 "
        "--reference_name 22 --start 51005491 --end 51005492 --page_size 1",
        "references-list-bases --id EIaSo62VtfXT4AE --start 15000 "
        "--end 15010",
        "referencesets-get --id EMud_c37lKPXTQ",
        "references-get --id EIaSo62VtfXT4AE",
        "variantsets-search --dataset_ids 10473108253681171589",
        "referencesets-search --accessions GCA_000001405.15",
        "references-search --md5checksums 1b22b98cdeb4a9304cb5d48026a85128",
        "readgroupsets-search --dataset_ids 10473108253681171589 "
        "--name NA12878 --page_size 1",
        "callsets-search --variant_set_ids 10473108253681171589 "
        "--name HG00261 --page_size 1",
        "reads-search --start 51005353 --end 51005354 --read_group_ids "
        "ChhDTXZuaHBLVEZoQ2JpT2J1enZtN25Pb0IQAA --reference_name "
        "22 --page_size 1",
    ]
    for command in commands:
        cmdStr = """
            python {path} {keyStr} {minimalOutput} {workarounds}
            {command} {baseUrl}
            """
        cmdDict = {
            "path": path,
            "command": command,
            "workarounds": workarounds,
            "keyStr": keyStr,
            "baseUrl": baseUrl,
            "minimalOutput": minimalOutput,
        }
        cmd = cmdStr.format(**cmdDict)
        splits = shlex.split(cmd)
        cleanCmd = ' '.join(splits)
        utils.log(separator)
        utils.log(cleanCmd)
        utils.log(separator)
        utils.runCommandSplits(splits)


if __name__ == '__main__':
    runTests()
