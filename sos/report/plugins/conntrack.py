# Copyright (C) 2017 Red Hat, Inc., Marcus Linden <mlinden@redhat.com>
# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import (Plugin, RedHatPlugin, DebianPlugin,
                                UbuntuPlugin, SuSEPlugin)


class Conntrack(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin, SuSEPlugin):

    short_desc = 'conntrack - netfilter connection tracking'

    plugin_name = 'conntrack'
    profiles = ('network', 'cluster')

    packages = ('conntrack-tools', 'conntrack', 'conntrackd')

    def setup(self):
        # Collect info from conntrackd
        self.add_copy_spec("/etc/conntrackd/conntrackd.conf")
        self.add_cmd_output([
            "conntrackd -s network",
            "conntrackd -s cache",
            "conntrackd -s runtime",
            "conntrackd -s link",
            "conntrackd -s rsqueue",
            "conntrackd -s queue",
            "conntrackd -s ct",
            "conntrackd -s expect",
        ])

        # Collect info from conntrack
        self.add_cmd_output([
            "conntrack -L -o extended",
            "conntrack -S",
        ])

# vim: set et ts=4 sw=4 :
