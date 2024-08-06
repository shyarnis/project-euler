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
    var target: int = 600851475143
    var i: int = 2

    while i * i < target:

        while target%i == 0:
            target /= i
        i += 1

    return target