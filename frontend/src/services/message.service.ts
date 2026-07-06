import { api } from "./api";

export const getMessages =
  async (
    conversationId: number
  ) => {

    const response =
      await api.get(
        `/messages/${conversationId}`
      );

    return response.data;
};