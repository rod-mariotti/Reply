#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Provider:
    def __init__(self, num_region):
        self.region = []

class Region:
    def __init__(self, prov_region_id, resources, num_pack, cost_pack, latency_pack):
        self.prov_region_id = prov_region_id
        self.resources = resources
        self.num_pack = num_pack
        self.cost_pack = cost_pack
		self.latency_pack = latency_pack

class Proj:
    def __inti__(self, penalty, country_id, request):
        # input
        self.penalty = penalty
        self.country_id = country_id
        self.request = request

        # output
        self.buy_list = [] # lista di liste da 3 elementi del tipo (prov_id, prov_reg_id, num_pack)




with open('input.in', encoding='utf-8') as input_file:

