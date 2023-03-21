def hex_to_bytes(val):
    if not val:
        return []
    val = val.strip()
    if val.startswith('0x'):
        val = val[2:]

    num_bytes = len(val) // 2
    bytes_ = []
    for i in range(num_bytes):
        bytes_.append(int(val[i*2:i*2+2], 16))
    return bytes_

def parse_little_endian_int32(buffer, offset):
    return (buffer[offset+3] << 24) + (buffer[offset+2] << 16) + (buffer[offset+1] << 8) + buffer[offset]

def parse_little_endian_int16(buffer, offset):
    return (buffer[offset+1] << 8) + buffer[offset]

def parse_little_endian_int16_bits(buffer, offset, bit_offset, bit_length):
    temp = parse_little_endian_int16(buffer, offset)
    temp = temp >> bit_offset
    mask = 0xffff >> (16 - bit_length)
    return temp & mask

def parse_sigfox(data):
    buffer = hex_to_bytes(data)

    if not buffer:
        return None

    record_type = buffer[0] & 0x0f

    if record_type == 0: #positional data
        return parse_positional_data(buffer)
    elif record_type == 1: #downlink ACK
        return parse_downlink_ack(buffer)
    elif record_type == 2: #device data
        return parse_device_stats(buffer)
    elif record_type == 3: #extended positional data
        return parse_extended_data(buffer)
    else:
        return None

def parse_positional_data(buffer):
    flags = buffer[0] & 0xF0
    in_trip = (flags & 0x10) > 0
    last_fix_failed = (flags & 0x20) > 0

    latitude_raw = parse_little_endian_int32(buffer, 1)
    longitude_raw = parse_little_endian_int32(buffer, 5)
    heading_raw = buffer[9]
    speed_raw = buffer[10]
    battery_raw = buffer[11]

    return {
        'MessageType': 0,
        'InTrip': in_trip,
        'LastFixFailed': last_fix_failed,
        'Latitude': latitude_raw * 1e-7,
        'Longitude': longitude_raw * 1e-7,
        'Heading': heading_raw * 2,
        'SpeedKmH': speed_raw,
        'BatteryVoltage': (battery_raw * 25) / 1000.0
    }

def parse_downlink_ack(buffer):
    flags = buffer[0] & 0xF0
    downlink_accepted = (flags & 0x10) > 0

    firmware_major = buffer[2]
    firmware_minor = buffer[3]

    data = [i+4 for i in range(8)]

    return {
        'MessageType': 1,
        'DownlinkAccepted': downlink_accepted,
        'FirmwareVersion': f"{firmware_major}.{firmware_minor}",
        'DownlinkData': data
    }

def parse_device_stats(buffer):
    uptime_weeks = parse_little_endian_int16_bits(buffer, 0, 4, 9)
    tx_count_raw = parse_little_endian_int16_bits(buffer, 1, 5, 11)
    rx_count_raw = buffer[3]
    trip_count_raw = parse_little_endian_int16_bits(buffer, 4, 0, 13)
    gps_success_raw = parse_little_endian_int16
