extends SceneTree


func _init() -> void:
    var start: float = Time.get_unix_time_from_system()
    var ans: int = solution()
    var finish: float = Time.get_unix_time_from_system()
    var duration: float = finish - start
    print("Answer     = %s" % ans)
    print("Time Taken = %.3f" % duration)
    quit()


func solution() -> int:
    var sum: int = 0

    for i in range(1, 1000):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
            
    return sum