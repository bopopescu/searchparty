# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to set IAM policy for a folder."""

from googlecloudsdk.api_lib.resource_manager import folders
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.command_lib.resource_manager import flags


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class SetIamPolicy(base.Command):
  """Set IAM policy for a folder.

  Sets the IAM policy for a folder, given a folder ID and a file encoded in
  JSON or YAML that contains the IAM policy.

  ## EXAMPLES

  The following command reads an IAM policy defined in a JSON file `policy.json`
  and sets it for a folder with the ID `3589215982`:

    $ {command} 3589215982 policy.json
  """

  @staticmethod
  def Args(parser):
    flags.FolderIdArg('whose policy you want to set.').AddToParser(parser)
    parser.add_argument(
        'policy_file', help='JSON or YAML file with the IAM policy')

  def Run(self, args):
    messages = folders.FoldersMessages()
    policy = iam_util.ParsePolicyFile(args.policy_file, messages.Policy)
    result = folders.SetIamPolicy(args.id, policy)
    iam_util.LogSetIamPolicy(args.id, 'folder')
    return result
