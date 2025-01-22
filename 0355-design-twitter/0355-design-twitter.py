class Twitter:

    def __init__(self):
        self.map = defaultdict(lambda: [[], set()]) 
        self.time = 0  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.map[userId][0].append((self.time, tweetId))
        self.time += 1

    def dfs(self, userId, res):
        for tweet in self.map[userId][0]:
            res.append(tweet)
        
        for nxt in list(self.map[userId][1]):
            for tweet in self.map[nxt][0]:
                res.append(tweet)
        res.sort(key=lambda x:x[0], reverse=True)
        while res and len(res) > 10:
            res.pop()
        
        return [x[1] for x in res]
    def getNewsFeed(self, userId: int) -> List[int]:
        return self.dfs(userId, [])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.map[followerId][1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.map[followerId][1].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)