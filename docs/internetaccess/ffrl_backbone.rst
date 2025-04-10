.. SPDX-License-Identifier: MIT
.. SPDX-FileCopyrightText: 2018, Sven Eckelmann <sven@narfation.org>

==================================
Freifunk Rheinland Backbone access
==================================

Assigned IPs
============

FFV-IPv4 1
  185.66.195.42/31
FFV-IPv4 2
  185.66.194.70/31
FFV-IPv6
  2a03:2260:200f::/48


AS
==

* FFV: 64857
* FFRL: 201701

GRE-Tunnel
==========

* Local  IP on vogtl-\*
* Remote IP on bb-\*

.. flat-table::
   :header-rows: 1

   * - :cspan:`1` FFRL-Server
     - vogtl-ffv01 (195.201.105.50)
     - vogtl-ffv02 (83.221.241.138)
     - vogtl-ffv04 (94.130.152.121)
     - vogtl-ffv05 (185.185.26.86)
     - vogtl-ffv06 (178.63.227.200)

   * - :rspan:`3` bb-a.ak.ber (185.66.195.0)
     - Local IPv4
     - 100.64.7.241/31
     - 100.64.7.229/31
     - 100.64.9.31/31
     - 100.64.9.191/31
     - 100.64.9.203/31

   * - Remote IPv4
     - 100.64.7.240/31
     - 100.64.7.228/31
     - 100.64.9.30/31
     - 100.64.9.190/31
     - 100.64.9.202/31

   * - Local IPv6
     - 2a03:2260:0:41a::2/64
     - 2a03:2260:0:414::2/64
     - 2a03:2260:0:4a4::2/64
     - 2a03:2260:0:4f4::2/64
     - 2a03:2260:0:4fa::2/64

   * - Remote IPv6
     - 2a03:2260:0:41a::1/64
     - 2a03:2260:0:414::1/64
     - 2a03:2260:0:4a4::1/64
     - 2a03:2260:0:4f4::1/64
     - 2a03:2260:0:4fa::1/64

   * - :rspan:`3` bb-a.fra2.fra (185.66.194.0)
     - Local IPv4
     - 100.64.7.243/31
     - 100.64.7.231/31
     - 100.64.9.33/31
     - 100.64.9.193/31
     - 100.64.9.205/31

   * - Remote IPv4
     - 100.64.7.242/31
     - 100.64.7.230/31
     - 100.64.9.32/31
     - 100.64.9.192/31
     - 100.64.9.204/31

   * - Local IPv6
     - 2a03:2260:0:41b::2/64
     - 2a03:2260:0:415::2/64
     - 2a03:2260:0:4a5::2/64
     - 2a03:2260:0:4f5::2/64
     - 2a03:2260:0:4fb::2/64

   * - Remote IPv6
     - 2a03:2260:0:41b::1/64
     - 2a03:2260:0:415::1/64
     - 2a03:2260:0:4a5::1/64
     - 2a03:2260:0:4f5::1/64
     - 2a03:2260:0:4fb::1/64

   * - :rspan:`3` bb-a.ix.dus (185.66.193.0)
     - Local IPv4
     - 100.64.7.245/31
     - 100.64.7.233/31
     - 100.64.9.35/31
     - 100.64.9.195/31
     - 100.64.9.207/31

   * - Remote IPv4
     - 100.64.7.244/31
     - 100.64.7.232/31
     - 100.64.9.34/31
     - 100.64.9.194/31
     - 100.64.9.206/31

   * - Local IPv6
     - 2a03:2260:0:41c::2/64
     - 2a03:2260:0:416::2/64
     - 2a03:2260:0:4a6::2/64
     - 2a03:2260:0:4f6::2/64
     - 2a03:2260:0:4fc::2/64

   * - Remote IPv6
     - 2a03:2260:0:41c::1/64
     - 2a03:2260:0:416::1/64
     - 2a03:2260:0:4a6::1/64
     - 2a03:2260:0:4f6::1/64
     - 2a03:2260:0:4fc::1/64

   * - :rspan:`3` bb-b.ak.ber (185.66.195.1)
     - Local IPv4
     - 100.64.7.247/31
     - 100.64.7.235/31
     - 100.64.9.37/31
     - 100.64.9.197/31
     - 100.64.9.209/31

   * - Remote IPv4
     - 100.64.7.246/31
     - 100.64.7.234/31
     - 100.64.9.36/31
     - 100.64.9.196/31
     - 100.64.9.208/31

   * - Local IPv6
     - 2a03:2260:0:41d::2/64
     - 2a03:2260:0:417::2/64
     - 2a03:2260:0:4a7::2/64
     - 2a03:2260:0:4f7::2/64
     - 2a03:2260:0:4fd::2/64

   * - Remote IPv6
     - 2a03:2260:0:41d::1/64
     - 2a03:2260:0:417::1/64
     - 2a03:2260:0:4a7::1/64
     - 2a03:2260:0:4f7::1/64
     - 2a03:2260:0:4fd::1/64

   * - :rspan:`3` bb-b.fra2.fra (185.66.194.1)
     - Local IPv4
     - 100.64.7.249/31
     - 100.64.7.237/31
     - 100.64.9.39/31
     - 100.64.9.199/31
     - 100.64.9.211/31

   * - Remote IPv4
     - 100.64.7.248/31
     - 100.64.7.236/31
     - 100.64.9.38/31
     - 100.64.9.198/31
     - 100.64.9.210/31

   * - Local IPv6
     - 2a03:2260:0:41e::2/64
     - 2a03:2260:0:418::2/64
     - 2a03:2260:0:4a8::2/64
     - 2a03:2260:0:4f8::2/64
     - 2a03:2260:0:4fe::2/64

   * - Remote IPv6
     - 2a03:2260:0:41e::1/64
     - 2a03:2260:0:418::1/64
     - 2a03:2260:0:4a8::1/64
     - 2a03:2260:0:4f8::1/64
     - 2a03:2260:0:4fe::1/64

   * - :rspan:`3` bb-b.ix.dus (185.66.193.1)
     - Local IPv4
     - 100.64.7.251/31
     - 100.64.7.239/31
     - 100.64.9.41/31
     - 100.64.9.201/31
     - 100.64.9.213/31

   * - Remote IPv4
     - 100.64.7.250/31
     - 100.64.7.238/31
     - 100.64.9.40/31
     - 100.64.9.200/31
     - 100.64.9.212/31

   * - Local IPv6
     - 2a03:2260:0:41f::2/64
     - 2a03:2260:0:419::2/64
     - 2a03:2260:0:4a9::2/64
     - 2a03:2260:0:4f9::2/64
     - 2a03:2260:0:4ff::2/64

   * - Remote IPv6
     - 2a03:2260:0:41f::1/64
     - 2a03:2260:0:419::1/64
     - 2a03:2260:0:4a9::1/64
     - 2a03:2260:0:4f9::1/64
     - 2a03:2260:0:4ff::1/64
