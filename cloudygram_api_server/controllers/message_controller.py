from pyramid_handlers               import action
from pyramid.request                import Request
from pyramid.httpexceptions         import HTTPUnauthorized
from cloudygram_api_server.models   import UserModels
from telethon.tl.types              import MessageMediaDocument
from cloudygram_api_server.scripts  import jres
import asyncio, concurrent.futures
import cloudygram_api_server

class MessageController(object):
    __autoexpose__ = None

    def __init__(self, request):
        self.request = request
        self.pool = concurrent.futures.ThreadPoolExecutor()
        self.wrap = cloudygram_api_server.get_tt()

    @action(name="getMessages", renderer="json", request_method="GET")
    def get_messages(self):
        phone_number= self.request.matchdict["phoneNumber"][1:]
        chat_id = self.request.GET["chatId"]
        self.wrap.create_session(phone_number) 
        self.pool.submit(
                asyncio.run,
                self.wrap.get_messages(chat_id)
                )
        return jres(HomeModels.success(message="messages downloaded..."))