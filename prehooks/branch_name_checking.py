import argparse
import re
from typing import AbstractSet
from typing import Optional
from typing import Sequence

from prehooks.utils import CalledProcessError
from prehooks.utils import cmd_output

regex = r'(^[0-9A-Za-z_]+-[0-9]+)\/[a-zA-Z0-9._-]+$'


def check_branch_name(
        excluded_branches: AbstractSet[str],
) -> int:
    try:
        ref_name = cmd_output('git', 'symbolic-ref', 'HEAD')
    except CalledProcessError:
        return 1
    chunks = ref_name.strip().split('/')
    branch_name = '/'.join(chunks[2:])
    if branch_name in excluded_branches or re.findall(regex, branch_name):
        return 0
    print('Something went wrong with the branch name. The branch name should start with'
          'Issue Id from Jira. Example: "DS-69/short_description"')
    return 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--exclude_branches', '-e', action='append',
        help='branch to disallow commits to, may be specified multiple times',
    )
    args = parser.parse_args(argv)

    excluded_branches = frozenset(args.exclude_branches or ('master', 'main', 'staging', 'develop', 'dev', 'stg'))
    return check_branch_name(excluded_branches)


if __name__ == '__main__':
    raise SystemExit(main())
