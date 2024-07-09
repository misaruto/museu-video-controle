from src.utils.video_handler_util import VideoHanlerUtil
from src.repository.rmi_server_session_repository import RmiServerSessionRepository
from sqlalchemy.exc import SQLAlchemyError

class RmiServerVideoControlServiceImpl:
  def __init__(self,session_repo:RmiServerSessionRepository) -> None:
    self.session_repo = session_repo

  def execute_command(self,command:str,session_token:str):
    try:
      self.auth_code,self.session,self.server = self.session_repo.find_active_session_by_token(session_token)
      self.video_handle = VideoHanlerUtil(self.server.nm_rmi_server_uri)
      self.video_handle.execute_command(command)
      return self.session,None
    except ValueError as e:
        return None,{'error': str(e)}
    except SQLAlchemyError as e:
        return None,{'error': 'Database error occurred', 'details': str(e)}
    except Exception as e:
        return None,str(e)