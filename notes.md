### Problem 001

-   sum of all divisible by `n` upto `target` is given by

    1. find `p`
        - p = target divide n
    2. use sum of N natural numbers upto `p` and multiply by `n`
        - ((p*(p+1))*0.5) \* n

-   Add sum divisible by `3` and sum divisible by `5` after that subtract sum divisible by `15`

-   sum divisible by `15` is required for subtactraction to avoid double counting the numbers that are divisible by both `3` and `5`.
