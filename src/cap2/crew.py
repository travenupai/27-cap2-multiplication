from crewai import Agent, Crew, Process, Task
from src.cap2.tools.math_tool import MultiplicationTool
from dotenv import load_dotenv
from crewai.project import CrewBase, agent, crew, task
from src.cap2.MyLLM import MyLLM
load_dotenv()
llm = MyLLM.gpt4o_mini
multiplication_tool = MultiplicationTool()


# Uncomment the following line to use an example of a custom tool
# from cap2.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class Cap2():
	"""Cap2 crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def generator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['generator_agent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=llm,
			allow_delegation=False
		)

	@agent
	def writer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['writer_agent'],
			tools=[multiplication_tool],
   			verbose=True,
			llm=llm,
			allow_delegation=False	
		)

	@task
	def generate_numbers_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_numbers_task'],
		)

	@task
	def multipication_task(self) -> Task:
		return Task(
			config=self.tasks_config['multiplication_task'],
			tools=[multiplication_tool],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Cap2 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
