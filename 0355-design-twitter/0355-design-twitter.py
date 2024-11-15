class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                min_heap.append(tweet)
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    for tweet in self.tweets[followeeId]:
                        min_heap.append(tweet)
        
        most_recent = heapq.nlargest(10, min_heap, key=lambda x: x[0])
        return [tweet[1] for tweet in most_recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)