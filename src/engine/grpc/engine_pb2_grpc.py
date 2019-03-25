# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

try:
    import engine_pb2 as engine__pb2
except:
    from engine.grpc import engine_pb2 as engine__pb2

class EngineStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DesktopGet = channel.unary_unary(
        '/engine.Engine/DesktopGet',
        request_serializer=engine__pb2.DesktopGetRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopGetResponse.FromString,
        )
    self.DesktopList = channel.unary_unary(
        '/engine.Engine/DesktopList',
        request_serializer=engine__pb2.Empty.SerializeToString,
        response_deserializer=engine__pb2.DesktopListResponse.FromString,
        )
    self.DesktopStart = channel.unary_unary(
        '/engine.Engine/DesktopStart',
        request_serializer=engine__pb2.DesktopStartRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopStartResponse.FromString,
        )
    self.DesktopViewer = channel.unary_unary(
        '/engine.Engine/DesktopViewer',
        request_serializer=engine__pb2.DesktopViewerRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopViewerResponse.FromString,
        )
    self.DesktopStop = channel.unary_unary(
        '/engine.Engine/DesktopStop',
        request_serializer=engine__pb2.DesktopStopRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopStopResponse.FromString,
        )
    self.DesktopDelete = channel.unary_unary(
        '/engine.Engine/DesktopDelete',
        request_serializer=engine__pb2.DesktopDeleteRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopDeleteResponse.FromString,
        )
    self.DesktopFromTemplate = channel.unary_unary(
        '/engine.Engine/DesktopFromTemplate',
        request_serializer=engine__pb2.DesktopFromTemplateRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopFromTemplateResponse.FromString,
        )
    self.DesktopFromMedia = channel.unary_unary(
        '/engine.Engine/DesktopFromMedia',
        request_serializer=engine__pb2.DesktopFromMediaRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopFromMediaResponse.FromString,
        )
    self.DesktopUpdate = channel.unary_unary(
        '/engine.Engine/DesktopUpdate',
        request_serializer=engine__pb2.DesktopUpdateRequest.SerializeToString,
        response_deserializer=engine__pb2.DesktopUpdateResponse.FromString,
        )
    self.TemplateGet = channel.unary_unary(
        '/engine.Engine/TemplateGet',
        request_serializer=engine__pb2.TemplateGetRequest.SerializeToString,
        response_deserializer=engine__pb2.TemplateGetResponse.FromString,
        )
    self.TemplateList = channel.unary_unary(
        '/engine.Engine/TemplateList',
        request_serializer=engine__pb2.Empty.SerializeToString,
        response_deserializer=engine__pb2.TemplateListResponse.FromString,
        )
    self.TemplateDelete = channel.unary_unary(
        '/engine.Engine/TemplateDelete',
        request_serializer=engine__pb2.TemplateDeleteRequest.SerializeToString,
        response_deserializer=engine__pb2.TemplateDeleteResponse.FromString,
        )
    self.TemplateUpdate = channel.unary_unary(
        '/engine.Engine/TemplateUpdate',
        request_serializer=engine__pb2.TemplateUpdateRequest.SerializeToString,
        response_deserializer=engine__pb2.TemplateUpdateResponse.FromString,
        )
    self.TemplateFromDomain = channel.unary_unary(
        '/engine.Engine/TemplateFromDomain',
        request_serializer=engine__pb2.TemplateFromDesktopRequest.SerializeToString,
        response_deserializer=engine__pb2.TemplateFromDesktopResponse.FromString,
        )
    self.BaseGet = channel.unary_unary(
        '/engine.Engine/BaseGet',
        request_serializer=engine__pb2.BaseGetRequest.SerializeToString,
        response_deserializer=engine__pb2.BaseGetResponse.FromString,
        )
    self.BaseList = channel.unary_unary(
        '/engine.Engine/BaseList',
        request_serializer=engine__pb2.Empty.SerializeToString,
        response_deserializer=engine__pb2.BaseListResponse.FromString,
        )


class EngineServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DesktopGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopViewer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopStop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopFromTemplate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopFromMedia(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DesktopUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TemplateGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TemplateList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TemplateDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TemplateUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TemplateFromDomain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BaseGet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BaseList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EngineServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DesktopGet': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopGet,
          request_deserializer=engine__pb2.DesktopGetRequest.FromString,
          response_serializer=engine__pb2.DesktopGetResponse.SerializeToString,
      ),
      'DesktopList': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopList,
          request_deserializer=engine__pb2.Empty.FromString,
          response_serializer=engine__pb2.DesktopListResponse.SerializeToString,
      ),
      'DesktopStart': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopStart,
          request_deserializer=engine__pb2.DesktopStartRequest.FromString,
          response_serializer=engine__pb2.DesktopStartResponse.SerializeToString,
      ),
      'DesktopViewer': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopViewer,
          request_deserializer=engine__pb2.DesktopViewerRequest.FromString,
          response_serializer=engine__pb2.DesktopViewerResponse.SerializeToString,
      ),
      'DesktopStop': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopStop,
          request_deserializer=engine__pb2.DesktopStopRequest.FromString,
          response_serializer=engine__pb2.DesktopStopResponse.SerializeToString,
      ),
      'DesktopDelete': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopDelete,
          request_deserializer=engine__pb2.DesktopDeleteRequest.FromString,
          response_serializer=engine__pb2.DesktopDeleteResponse.SerializeToString,
      ),
      'DesktopFromTemplate': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopFromTemplate,
          request_deserializer=engine__pb2.DesktopFromTemplateRequest.FromString,
          response_serializer=engine__pb2.DesktopFromTemplateResponse.SerializeToString,
      ),
      'DesktopFromMedia': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopFromMedia,
          request_deserializer=engine__pb2.DesktopFromMediaRequest.FromString,
          response_serializer=engine__pb2.DesktopFromMediaResponse.SerializeToString,
      ),
      'DesktopUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.DesktopUpdate,
          request_deserializer=engine__pb2.DesktopUpdateRequest.FromString,
          response_serializer=engine__pb2.DesktopUpdateResponse.SerializeToString,
      ),
      'TemplateGet': grpc.unary_unary_rpc_method_handler(
          servicer.TemplateGet,
          request_deserializer=engine__pb2.TemplateGetRequest.FromString,
          response_serializer=engine__pb2.TemplateGetResponse.SerializeToString,
      ),
      'TemplateList': grpc.unary_unary_rpc_method_handler(
          servicer.TemplateList,
          request_deserializer=engine__pb2.Empty.FromString,
          response_serializer=engine__pb2.TemplateListResponse.SerializeToString,
      ),
      'TemplateDelete': grpc.unary_unary_rpc_method_handler(
          servicer.TemplateDelete,
          request_deserializer=engine__pb2.TemplateDeleteRequest.FromString,
          response_serializer=engine__pb2.TemplateDeleteResponse.SerializeToString,
      ),
      'TemplateUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.TemplateUpdate,
          request_deserializer=engine__pb2.TemplateUpdateRequest.FromString,
          response_serializer=engine__pb2.TemplateUpdateResponse.SerializeToString,
      ),
      'TemplateFromDomain': grpc.unary_unary_rpc_method_handler(
          servicer.TemplateFromDomain,
          request_deserializer=engine__pb2.TemplateFromDesktopRequest.FromString,
          response_serializer=engine__pb2.TemplateFromDesktopResponse.SerializeToString,
      ),
      'BaseGet': grpc.unary_unary_rpc_method_handler(
          servicer.BaseGet,
          request_deserializer=engine__pb2.BaseGetRequest.FromString,
          response_serializer=engine__pb2.BaseGetResponse.SerializeToString,
      ),
      'BaseList': grpc.unary_unary_rpc_method_handler(
          servicer.BaseList,
          request_deserializer=engine__pb2.Empty.FromString,
          response_serializer=engine__pb2.BaseListResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'engine.Engine', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
