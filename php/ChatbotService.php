<?php

declare(strict_types=1);

final class ChatbotService
{
    public function normalize(string $message): string
    {
        $message = trim($message);

        if ($message === '') {
            throw new InvalidArgumentException('Message cannot be empty.');
        }

        return preg_replace('/\\s+/', ' ', $message) ?? $message;
    }

    public function buildRequest(string $message, ?string $conversationId = null): array
    {
        return [
            'conversation_id' => $conversationId,
            'message' => $this->normalize($message),
        ];
    }
}
