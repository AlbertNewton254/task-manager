import type { Task, TaskCreate } from '../types/task';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const api = {
  // Get all tasks
  getTasks: async (): Promise<Task[]> => {
    const response = await fetch(`${API_BASE_URL}/tasks`);
    if (!response.ok) throw new Error('Failed to fetch tasks');
    return response.json();
  },

  // Create a new task
  createTask: async (task: TaskCreate): Promise<Task> => {
    const response = await fetch(`${API_BASE_URL}/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(task),
    });
    if (!response.ok) throw new Error('Failed to create task');
    return response.json();
  },

  // Update a task
  updateTask: async (id: number, task: TaskCreate): Promise<Task> => {
    const response = await fetch(`${API_BASE_URL}/task/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(task),
    });
    if (!response.ok) throw new Error('Failed to update task');
    return response.json();
  },

  // Toggle task completion
  toggleTaskCompletion: async (id: number): Promise<Task> => {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}/complete`, {
      method: 'PATCH',
    });
    if (!response.ok) throw new Error('Failed to toggle task completion');
    return response.json();
  },

  // Delete a task
  deleteTask: async (id: number): Promise<void> => {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete task');
  },
};
