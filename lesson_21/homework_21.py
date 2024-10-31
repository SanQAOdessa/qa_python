import logging
from datetime import datetime, timedelta



def get_hb_data_from_file():
    with open('hblog.txt') as f:
        filtered_log = []
        for row in f:
            if 'TSTFEED0300|7E3E|0400' in row:
                start_time_pos = row.find("Timestamp ") + 10
                end_time_pos = row.find("Timestamp ") + 18
                filtered_log.append(datetime.strptime(row[start_time_pos: end_time_pos], "%H:%M:%S")
)
    return filtered_log

if __name__ == '__main__':
    logging.basicConfig(filename='hb_test.log', format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    log = get_hb_data_from_file()
    end_time = False
    for start_time in log:
        if end_time:
            diff_time = end_time - start_time
            message = f" difference is {diff_time} at {end_time.strftime('%H:%M:%S')} from {start_time.strftime('%H:%M:%S')}"

            if diff_time == timedelta(seconds=32):
                logger.warning(message)
            elif diff_time >= timedelta(seconds=33):
                logger.error(message)

            end_time = start_time
        else:
            end_time = start_time