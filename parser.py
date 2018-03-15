#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Provider:
    def __init__(self, num_region):
        self.num_region = num_region
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


def read_provider(filename, provider_list):
    line = filename.readline().rstrip()
    line = line.split( )
    line[1] = int(line[1])

    provider_list.append(Provider(line[1]))

def read_region(filename, provider_region_list, region_id, services_num):
    line_a = filename.readline().rstrip()
    line_a = line_a.split( )

    line_b = filename.readline().rstrip()
    line_b = line_b.split( )

    provider_region_list.append(Region(region_id, line_a[-services_num:], line_a[0], line_a[1], line_b))
    

with open('input.in', encoding='utf-8') as input_file:
    first_line = input_file.readline().rstrip()
    first_line = first_line.split( )

    provider_num, services_num, countries_num, proj_num = [int(i) for i in first_line] 

    provider = []
    proj = [None for i in range(proj_num)]

    input_file.readline()
    input_file.readline()
    
    for prov in range(provider_num - 1):
        read_provider(input_file, provider)

        for reg in range(provider[prov].num_region):
            input_file.readline() # salta nome regione
            read_region(input_file, provider[prov].region, reg, services_num)

print(provider[1].region[0].resources)
