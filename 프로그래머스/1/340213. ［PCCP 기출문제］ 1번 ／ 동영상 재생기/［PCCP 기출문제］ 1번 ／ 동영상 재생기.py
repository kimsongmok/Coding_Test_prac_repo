def to_seconds(time_str):
    """ 시간을 'mm:ss' 형식에서 초로 변환하는 함수 """
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

def to_time_str(seconds):
    """ 초를 다시 'mm:ss' 형식으로 변환하는 함수 """
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def solution(video_len, pos, op_start, op_end, commands):
    # 입력값을 초 단위로 변환
    video_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)
    
    # 오프닝 구간에 있는지 먼저 확인하여 이동
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    
    # 명령어 처리
    for command in commands:
        if command == "next":
            pos_sec = min(pos_sec + 10, video_len_sec)  # 10초 후로 이동, 영상 끝을 넘지 않도록
        elif command == "prev":
            pos_sec = max(pos_sec - 10, 0)  # 10초 전으로 이동, 0분 0초보다 이전으로 가지 않도록

        # 이동 후에 다시 오프닝 구간 안에 있는지 확인
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec  # 오프닝 구간이면 오프닝 끝 시각으로 이동

    # 결과를 "mm:ss" 형식으로 반환
    return to_time_str(pos_sec)