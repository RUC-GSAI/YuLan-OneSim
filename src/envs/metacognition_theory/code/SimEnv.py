from onesim.simulator import BasicSimEnv
from onesim.events import Event
from .events import StartEvent
from datetime import datetime

class SimEnv(BasicSimEnv):
    async def _create_start_event(self, target_id: str) -> Event:
        # Extract relevant information from self.data according to StartEvent
        source_id = self.data.get('environment_id', 'ENV')
        task_type = self.data.get('task_type', 'default_task')
        timestamp = datetime.now()
        
        return StartEvent(
            from_agent_id=source_id,
            to_agent_id=target_id,
            task_type=task_type,
            timestamp=timestamp
        )