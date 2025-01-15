/**  @odoo-module **/
import {registry} from '@web/core/registry';
import {useService} from "@web/core/utils/hooks";

const {Component, useState, onWillStart, useRef} = owl;

export class TodoTask extends Component {
  setup() {
    this.state = useState({
      task: {
        name: "",
        color: "",
        is_done: false,
        description: "",
      },
      taskList: [],
      isEdit: false,
      activeId: false,
    });

    this.orm = useService('orm');
    this.model = 'todo.task';
    this.searchInput = useRef("search-input");

    onWillStart(async () => {
      await this.getAllTasks();
    });
  }

  async getAllTasks() {
    this.state.taskList = await this.orm.searchRead(this.model, [], [
      "name",
      "color",
      "is_done",
      "description",
    ]);
  }

  addTask() {
    this.resetForm();
    this.state.isEdit = false;
    this.state.activeId = false;
  }

  editTask(task) {
    this.state.task = {...task}; // Ensure the task state is updated without reference issues
    this.state.isEdit = true;
    this.state.activeId = task.id;
  }

  async saveTask() {
    try {
      if (this.state.isEdit) {
        await this.orm.write(this.model, [this.state.activeId],
            this.state.task);
        this.state.isEdit = false;
      } else {
        await this.orm.create(this.model, this.state.task);
        this.resetForm();
      }
      await this.getAllTasks();
    } catch (error) {
      console.error("Error saving task:", error);
      alert("An error occurred while saving the task.");
    }
  }

  async deleteTask(task) {
      await this.orm.unlink(this.model, [task.id])
      await this.getAllTasks()
  }

  async searchTasks() {
    const text = this.searchInput.el.value;
    this.state.taskList = await this.orm.searchRead(this.model, [["name", "ilike", text]], ["name", "color", "is_done", "description"])
  }

  async updateColor(e, task) {
    await this.orm.write(this.model, [task.id], {color: e.target.value})
    await this.getAllTasks()
  }

  resetForm() {
    this.state.task = {
      name: "",
      color: "#000000",
      is_done: false,
      description: "",
    };
  }
}

TodoTask.template = "education.TodoTask";
registry.category("actions").add("education.todo_task_action_js", TodoTask);
