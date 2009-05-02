#!/usr/bin/env python

from twisted.words.xish import domish

from wokkel import pubsub

class PubSubProtocol(pubsub.PubSubClient):

    connected = False

    def connectionInitialized(self):
        self.connected = True

    def connectionLost(self):
        self.connected = False

    def gotEntry(self, entry, service, node):
        if self.connected:
            status = domish.Element(('http://twitterspy.org/entry', 'status'))
            status['user'] = entry.user.screen_name
            status.addContent(entry.text)

            item = pubsub.Item(entry.id, status)
            self.publish(service, node, [item])
