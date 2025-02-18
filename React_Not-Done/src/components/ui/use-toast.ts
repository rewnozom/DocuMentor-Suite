export const useToast = () => {
    const toast = ({
      title,
      description,
      variant,
    }: {
      title: string;
      description: string;
      variant: string;
    }) => {
      console.log(`[${variant}] ${title}: ${description}`);
      // Här kan du utöka med en riktig implementation (exempelvis med react-hot-toast).
    };
    return { toast };
  };
  